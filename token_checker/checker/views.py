from django.shortcuts import render, redirect
from .models import Token
from django.shortcuts import render, redirect

def home(request):
    if request.method == 'POST':
        contract_address = request.POST.get('contract_address')
        # Check if the contract_address is not empty before redirecting
        if contract_address:
            return render(request, 'home.html', {'contract_address': contract_address})

    return render(request, 'home.html')

def select_website(request):
    # Add logic here to render a template where users select the website
    return render(request, 'select_website.html')

def redirect_to_website(request, website, contract_address):
    # Logic to construct the URL based on the selected website and contract address
    if website == 'solscan':
        solscan_url = f'https://solscan.io/token/{contract_address}'
        return redirect(solscan_url)
    elif website == 'rugcheck':
        rugcheck_url = f'https://rugcheck.xyz/tokens/{contract_address}'
        return redirect(rugcheck_url)
    elif website == 'birdeye':
        birdeye_url = f'https://birdeye.so/token/{contract_address}'
        return redirect(birdeye_url)
    elif website == 'dextools':
        dextools_url = f'https://www.dextools.io/app/en/solana/pair-explorer/{contract_address}'
        return redirect(dextools_url)
    elif website == 'dexscreener':
        dexscreener_url = f'https://dexscreener.com/solana/{contract_address}'
        return redirect(dexscreener_url)

    return redirect('home')  # Redirect back to the home page if the website is not recognized

