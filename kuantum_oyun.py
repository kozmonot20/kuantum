from qiskit import QuantumCircuit
import numpy as np

print("--- KUANTUM YAPAY ZEKA MODELI ---")

# Yapay zekanın eğitilecek verisi (0 veya 1)
veri = 1 
print(f"Yapay zekaya ogretilen gizli veri: {veri}")

# Kuantum Yapay Zeka Devresi
qc = QuantumCircuit(1)

# Eğer veri 1 ise, kubiti X kapısı ile ters çeviriyoruz (Öğrenme aşaması)
if veri == 1:
    qc.x(0)

# Yapay zekanın ağırlık parametresi (Kuantum nöronu gibi düşün)
# Kubiti 180 derece (pi) döndürerek veriyi tahmin etmeye çalışıyor
aci = np.pi 
qc.rx(aci, 0)

qc.measure_all()
print("\n[BAŞARILI]: Kuantum Yapay Zeka Ağı kuruldu kanka!")
print(qc)
