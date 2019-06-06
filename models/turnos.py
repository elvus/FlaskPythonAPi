import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'hangvirus'


class Turnos(Base):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    nro_turno = columns.Text()
    fecha = columns.Text()
    hora = columns.Text()
    medico = columns.Text()
    persona = columns.Text()
    estado_turnos = columns.Text()

    def get_data(self):
        return {
            'id': str(self.id),
            'nro_turno': self.nro_turno,
            'fecha': self.fecha,
            'hora': self.hora,
            'medico': self.medico,
            'persona': self.persona,
            'estado': self.estado_turnos
        }