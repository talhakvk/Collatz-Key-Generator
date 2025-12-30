def generate_collatz_key(seed: int, length: int) -> str:
    """
    Collatz Sanrısı (3n+1) kullanarak rastgele bit dizisi üretir.
    """
    key_bits = []
    current = seed
    
    while len(key_bits) < length:
        # Sayı çift ise n/2, tek ise 3n+1
        if current % 2 == 0:
            current = current // 2
        else:
            current = (current * 3) + 1
        
        # Sayının son bitini (tek/çift durumu) anahtara ekle
        # 0 = Çift, 1 = Tek
        bit = str(current % 2)
        key_bits.append(bit)
        
        # Collatz dizisi 1'e ulaştığında 4-2-1 döngüsüne girer.
        # Bunu kırmak için seed'i manipüle ederek devam ediyoruz.
        if current == 1:
            current = seed + len(key_bits)

    return "".join(key_bits)

def binary_to_hex(binary_string: str) -> str:
    """Üretilen bit dizisini daha okunaklı olan Hexadecimal formata çevirir."""
    decimal_value = int(binary_string, 2)
    return hex(decimal_value).upper().replace("0X", "")

# --- Ana Program ---
if __name__ == "__main__":
    print("--- Collatz Anahtar Üreteci (Python) ---")
    
    try:
        user_seed = int(input("Başlangıç sayısı (Seed) girin: "))
        user_length = int(input("Üretilecek bit uzunluğunu girin (örn: 64, 128): "))
        
        generated_key = generate_collatz_key(user_seed, user_length)
        
        print(f"\n[+] Üretilen {user_length} Bitlik Anahtar (Binary):")
        print(generated_key)
        
        print(f"\n[+] Anahtar (Hex Formatı):")
        print(binary_to_hex(generated_key))
        
    except ValueError:
        print("Lütfen geçerli bir tam sayı girin!")


