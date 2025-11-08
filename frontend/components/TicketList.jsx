import React from 'react';
import api from '../api';

// Duruma göre renkli etiket döndüren yardımcı fonksiyon
const StatusBadge = ({ durum }) => {
  let className = 'badge-secondary';
  if (durum === 'Aktif') className = 'badge-success';
  if (durum === 'Arızalı') className = 'badge-danger';
  return <span className={`badge ${className}`}>{durum}</span>;
};

function TicketList({ tickets, onTicketResolved }) {
  
  const handleResolve = async (ticketId) => {
    if (!confirm("Bu arıza kaydını 'Çözüldü' olarak işaretlemek istediğinizden emin misiniz?")) {
      return;
    }
    try {
      await api.put(`/tickets/${ticketId}/resolve`);
      onTicketResolved(); // Başarılı olunca App.jsx'teki fonksiyonu tetikle
    } catch (error) {
      console.error("Arıza çözülemedi:", error);
      alert("Hata: " + error.response.data.detail);
    }
  };

  return (
    <div>
      <h2>Aktif Arıza Kayıtları</h2>
      <table>
        <thead>
          <tr>
            <th>Cihaz</th>
            <th>Açıklama</th>
            <th>Bildiren</th>
            <th>Cihaz Durumu</th>
            <th>İşlem</th>
          </tr>
        </thead>
        <tbody>
          {tickets.length === 0 ? (
            <tr><td colSpan="5" style={{ textAlign: 'center' }}>Aktif arıza kaydı yok.</td></tr>
          ) : (
            tickets.map(ticket => (
              <tr key={ticket.id}>
                <td>{ticket.cihaz.marka_model} (ID: {ticket.cihaz.id})</td>
                <td>{ticket.aciklama}</td>
                <td>{ticket.bildiren}</td>
                <td><StatusBadge durum={ticket.cihaz.durum} /></td>
                <td>
                  <button className="resolve" onClick={() => handleResolve(ticket.id)}>
                    Çözüldü İşaretle
                  </button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}

export default TicketList;