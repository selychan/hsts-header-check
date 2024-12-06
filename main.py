import requests

def print_banner():
    banner = """
    ###########################################################
    #                                                         #
    #                  H T S T  C H E C K E R              #
    #             -------------------------------          #
    #            Check if your website supports HSTS         #
    #                                                         #
    ###########################################################
    """
    print(banner)

def check_hsts(url):
    try:
        # URL'ye HTTPS isteği gönder
        response = requests.get(url, timeout=10)

        # Response header'larında HSTS kontrolü
        if "Strict-Transport-Security" in response.headers:
            print(f"HSTS header mevcut: {response.headers['Strict-Transport-Security']}")
        else:
            print("HSTS header eksik! Sunucu HSTS kullanmıyor.")
    except requests.exceptions.RequestException as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":

    print_banner()
    # Kullanıcıdan URL alma
    url = input("Lütfen kontrol etmek istediğiniz HTTPS URL'sini girin: ").strip()
    # URL'yi kontrol et
    if url.startswith("https://"):
        check_hsts(url)
    else:
        print("Lütfen geçerli bir HTTPS URL'si girin (https:// ile başlamalı).")
