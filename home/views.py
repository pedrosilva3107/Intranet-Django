import subprocess
import winrm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pop  # Certifique-se de que o modelo 'Pop' está corretamente importado

# Função para verificar se o servidor está online
def is_server_online(server_ip):
    try:
        # Usando o comando 'ping' para verificar se o servidor está ativo
        response = subprocess.run(
            ["ping", "-n", "1", server_ip],  # '-n' no Windows, '-c' em Linux
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return response.returncode == 0  # Se o código de retorno for 0, o servidor está online
    except Exception as e:
        print(f"Erro ao verificar servidor: {e}")
        return False

# Função para renderizar a página inicial (Home)
@login_required
def home(request):
    # IPs ou nomes dos servidores (Agora são 7 servidores)
    servidores = {
        "Servidor 1": "192.168.25.240",
        "Servidor 2": "192.168.0.2",
        "Servidor 3": "192.168.1.3",
        "Servidor 4": "192.168.1.4",
        "Servidor 5": "192.168.1.5",
        "Servidor 6": "192.168.1.6",
        "Servidor 7": "192.168.1.7"
    }

    # Verificar o status dos servidores
    server_status = {}
    for nome, ip in servidores.items():
        server_status[nome] = "ON" if is_server_online(ip) else "OFF"

    # Passar as informações para o template
    context = {
        'server_status': server_status,
    }

    return render(request, 'home.html', context)

# Função para reiniciar o servidor Windows via WinRM
@login_required
def reiniciar_servidor(request):
    try:
        # Detalhes do servidor Windows
        ip_remoto = "192.168.25.240"
        usuario = "pedro.silva"  # Substitua pelo nome de usuário no Windows
        senha = "Pedr1234"  # Substitua pela senha do usuário

        # Criar uma conexão com o servidor remoto usando WinRM
        sessao = winrm.Session(f'http://{ip_remoto}:5985/wsman', auth=(usuario, senha), server_cert_validation='ignore')

        # Comando para reiniciar o servidor Windows
        comando_reinicio = 'shutdown.exe /r /f /t 1'

        # Executar o comando
        resultado = sessao.run_cmd(comando_reinicio)

        # Verificar se o comando foi executado com sucesso
        if resultado.status_code == 0:
            return HttpResponse("Servidor reiniciado com sucesso.")
        else:
            return HttpResponse(f"Erro ao reiniciar o servidor: {resultado.std_err.decode()}")
    
    except winrm.exceptions.WinRMTransportError as e:
        # Erro de conexão WinRM
        return HttpResponse(f"Erro de conexão com o servidor via WinRM: {str(e)}")
    except Exception as e:
        # Outros erros
        return HttpResponse(f"Erro ao conectar ao servidor: {str(e)}")

# Função para consultar os POPs (geralmente para uma interface de gerenciamento)
@login_required  # Garante que apenas usuários logados possam acessar
def consultar_pops(request):
    pops = Pop.objects.all()  # Recupera todos os objetos do modelo Pop
    return render(request, 'consultar_pops.html', {'pops': pops})  # Passa os dados para o template
