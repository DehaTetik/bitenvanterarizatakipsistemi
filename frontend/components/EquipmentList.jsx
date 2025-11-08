import React, { useState } from 'react';
import api from '../api';

// Duruma göre renkli etiket
const StatusBadge = ({ durum }) => {
  let className = 'badge-secondary';
  if (durum === 'Aktif') className = 'badge-success';
  if (durum === 'Arızalı') className = 'badge-danger';
  return <span className={`badge ${className}`}>{durum}</span>;
};

function EquipmentList({ equipment, onEquipmentAdded }) {
  const [cihazTuru, setCihazTuru] = useState('');
  const [markaModel, setMarkaModel] = useState('');
  const [zimmetli, setZimmetli] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!cihazTuru || !markaModel || !zimmetli) {
      alert("Lütfen tüm alanları doldurun.");
      return;
    }
    
    const newEquipment = {
      cihaz_turu: cihazTuru,
      marka_model: markaModel,
      zimmetli_personel: zimmetli,
      // Durum, API tarafından otomatik 'Depoda' olarak atanacak
    };

    try {
      await api.post('/equipment', newEquipment);
      onEquipmentAdded(); // Liste yenile
      // Formu temizle
      setCihazTuru('');
      setMarkaModel('');
      setZimmetli('');
    } catch (error) {
      console.error("Ekipman eklenemedi:", error);
    }
  };

  return (
    <div>
      <h2>Yeni Ekipman Ekle</h2>
      <form onSubmit={handleSubmit} style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        <input 
          type="text" value={cihazTuru} onChange={e => setCihazTuru(e.target.value)}
          placeholder="Cihaz Türü (örn: PC)" required
        />
        <input 
          type="text" value={markaModel} onChange={e => setMarkaModel(e.target.value)}
          placeholder="Marka/Model (örn: HP ProDesk)" required
        />
        <input 
          type="text" value={zimmetli} onChange={e => setZimmetli(e.target.value)}
          placeholder="Zimmetli Personel (örn: Depo)" required
        />
        <button type="submit">Ekle</button>
      </form>

      <h2>Tüm Envanter</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Cihaz Türü</th>
            <th>Marka/Model</th>
            <th>Zimmetli</th>
            <th>Durum</th>
          </tr>
        </thead>
        <tbody>
          {equipment.map(item => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.cihaz_turu}</td>
              <td>{item.marka_model}</td>
              <td>{item.zimmetli_personel}</td>
              <td><StatusBadge durum={item.durum} /></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default EquipmentList;