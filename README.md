# Collatz-Key-Generator
# Collatz Conjecture Based Key Generator

Bu proje, matematik dünyasının ünlü **Collatz Sanrısı ($3n+1$)** algoritmasını kullanarak deterministik ancak kaotik bir yapıda **Pseudo-Random (Sözde Rastgele)** bit dizileri ve kriptografik anahtarlar üretir.

## 🚀 Proje Hakkında
Bu algoritma, verilen bir başlangıç sayısı (seed) üzerinden Collatz dizisinin adımlarını takip eder. Her adımda elde edilen sayının paritesini (tek veya çift olma durumu) bir bit olarak işleyerek, istenilen uzunlukta (64-bit, 128-bit vb.) binary ve hexadecimal anahtarlar oluşturur.

### Temel Özellikler
- **Dinamik Uzunluk:** Kullanıcıdan alınan girdi doğrultusunda istenen uzunlukta anahtar üretimi.
- **Döngü Kırıcı (Cycle Breaker):** Collatz dizisinin doğası gereği girdiği 4-2-1 kısırdöngüsünü, seed değerini kullanarak otomatik olarak kırar ve üretimin devamlılığını sağlar.
- **Çift Çıktı Formatı:** Hem ham Binary dizisi hem de okunabilirliği yüksek Hexadecimal format sunar.

## 🛠️ Algoritma Mantığı
1. Kullanıcıdan bir `Seed` ve `Bit Uzunluğu` alınır.
2. Sayı çift ise $n = n / 2$, tek ise $n = 3n + 1$ uygulanır.
3. Her sonucun $mod 2$ değeri (0 veya 1) anahtar dizisine eklenir.
4. Eğer sayı $1$'e ulaşırsa, döngüye girmemek için `Seed + Mevcut Uzunluk` formülüyle yeni bir sayı atanır.
5. İstenen uzunluğa ulaşıldığında dizi Hexadecimal formatına çevrilir.

## 📊 Akış Şeması (Flowchart)
Algoritmanın işleyişini gösteren akış şeması aşağıdadır:

```mermaid
flowchart TD
    StartNode([BAŞLAT]) --> Input[/Seed ve Bit Uzunluğu Gir/]
    Input --> LoopDecision{İstenen Uzunluğa<br/>Ulaşıldı mı?}
    LoopDecision -- Hayır --> Parity{Sayı Çift mi?}
    Parity -- Evet --> Even[n = n / 2]
    Parity -- Hayır --> Odd[n = 3n + 1]
    Even --> AddBit[Sayının Mod 2 değerini<br/>Anahtara Ekle]
    Odd --> AddBit
    AddBit --> CheckOne{n == 1?}
    CheckOne -- Evet --> Reset[n = Seed + Mevcut Uzunluk<br/>Döngü Kırıcı]
    CheckOne -- Hayır --> LoopDecision
    Reset --> LoopDecision
    LoopDecision -- Evet --> ToHex[Binary Dizisini<br/>Hexadecimal'e Çevir]
    ToHex --> Output[/Final Anahtarı Yazdır/]
    Output --> EndNode([BİTİŞ])
