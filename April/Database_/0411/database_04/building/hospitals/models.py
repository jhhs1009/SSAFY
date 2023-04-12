from django.db import models

# Create your models here.
# 1:N 배운 것으로 구현
class Doctor(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return f"{self.name} 전문의"

# 외래키 삭제
class Patient(models.Model):
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()
    
    def __str__(self):
        return f"{self.pk}번 환자 {self.name}"

# 중개모델 작성
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
    