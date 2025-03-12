from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, MetaData, create_engine
from sqlalchemy.orm import relationship, declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
engine = create_engine('sqlite:///theater.db')
Base.metadata.create_all(engine)

class Audition(Base):
  __tablename__ = "auditions"
  
  id = Column(Integer, primary_key = True, autoincrement = True)
  actor = Column(String(),primary_key=True)
  location = Column(String())
  phone = Column(Integer())
  hired = Column(Boolean, default = False)
  role_id = Column(Integer, ForeignKey("roles.id"))

  role = relationship("Role", back_populates="auditions")
  

  
  def call_back(self):
    self.hired = True
    



class Role(Base):
  __tablename__ = "roles"

  character_name = Column(String())

  auditions = relationship("Audition",back_populates="role")

  def auditions(self):
    return [audition for audition in self.auditions]
    
  
  def actors(self):
    return [audition.actor for audition in self.auditions]
    
  
  def locations(self):
    return [audition.location for audition in self.auditions]
    
  
  def lead(self):
     hired_auditions = [audition for audition in self.auditions if audition.hired]
     return hired_auditions[0] if hired_auditions else "No actor has been hired for this role"
  
  def understudy(self):
     hired_auditions = [audition for audition in self.auditions if audition.hired]
     return hired_auditions[1] if len(hired_auditions) > 1 else "No actor has been hired for understudy for this role"
    


 