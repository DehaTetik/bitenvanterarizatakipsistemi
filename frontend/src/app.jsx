import { useState, useEffect } from 'react';
import api from './api';
import TicketList from './components/TicketList';
import EquipmentList from './components/EquipmentList';

function App() {
  const [tickets, setTickets] = useState([]);
  const [equipment, setEquipment] = useState([]);
  const [loading, setLoading] = useState(true);

  // Veri çekme fonksiyonu
  const fetchData = async () => {
    setLoading(true);
    try {
      // API'den hem arızaları hem de envanteri aynı anda çek
      const [ticketsRes, equipmentRes] = await Promise.all([
        api.get('/tickets'), // Tüm arızaları çek
        api.get('/equipment') // Tüm envanteri çek
      ]);
      
      // 'Açık' olanları ayır (veya tümünü göster)
      setTickets(ticketsRes.data.filter(t => t.durum === 'Açık'));
      setEquipment(equipmentRes.data);
      
    } catch (error) {
      console.error("Veri çekilemedi:", error);
    } finally {
      setLoading(false);
    }
  };

  // 1. Bileşen ilk yüklendiğinde veriyi çek
  useEffect(() => {
    fetchData();
  }, []);

  // 2. Bir arıza çözüldüğünde veriyi yenile
  const handleTicketResolved = () => {
    fetchData(); // Tüm veriyi tazeleyerek senkronize kal
  };
  
  // 3. Yeni ekipman eklendiğinde veriyi yenile
  const handleEquipmentAdded = () => {
    fetchData();
  };

  if (loading) {
    return <h1>Yükleniyor...</h1>;
  }

  return (
    <>
      <h1>BİT Envanter ve Arıza Takip Sistemi</h1>
      <main>
        <section>
          {/* Arızaları listeleyen ve "Çöz" butonu olan bileşen */}
          <TicketList tickets={tickets} onTicketResolved={handleTicketResolved} />
        </section>
        <section>
          {/* Envanteri listeleyen ve yeni envanter ekleme formu olan bileşen */}
          <EquipmentList equipment={equipment} onEquipmentAdded={handleEquipmentAdded} />
        </section>
      </main>
    </>
  );
}

export default App;