from django.db import models
import telepot
from django.core.mail import send_mail
# Create your models here.


"""class RegUser(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    #Contact = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)"""

class RegiUser(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    receId = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)


class BPM(models.Model):
    bpm = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)

    def get_dt_display(self):
        return self.dt.strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return str(self.bpm)

    def save(self, *args, **kwargs):
        if self.bpm > 100:
            token = '5877186104:AAESpMPMIk6dvUILilf3aJ68Winv-79W36Q'
            rece_id = 1913801730
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id,'Cher [nom du patient], nous avons détecté que votre rythme cardiaque est supérieur à 100 bpm. Nous vous recommandons de consulter votre médecin dès que possible pour évaluer votre état de santé. Si vous ressentez des symptômes tels que des vertiges ou des douleurs thoraciques, veuillez contacter immédiatement votre médecin ou les services d"urgence. Prenez soin de vous. BPM = ' + str(self.bpm))
            send_mail(
                'BPM critique !!',
                'Cher [nom du patient], nous avons détecté que votre rythme cardiaque est supérieur à 100 bpm. Nous vous recommandons de consulter votre médecin dès que possible pour évaluer votre état de santé. Si vous ressentez des symptômes tels que des vertiges ou des douleurs thoraciques, veuillez contacter immédiatement votre médecin ou les services d"urgence. Prenez soin de vous.. BPM critique = ' + str(self.bpm),
                'amine.berrfai@ump.ac.ma',
                ['amineberrfai62@gmail.com'],
                fail_silently=False,
            )
        elif self.bpm < 60:
            token = '5877186104:AAESpMPMIk6dvUILilf3aJ68Winv-79W36Q'
            rece_id = 1913801730
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id,'Attention, votre fréquence cardiaque est anormalement basse. Nous vous recommandons de consulter votre médecin dès que possible. BPM = ' + str(self.bpm))
            send_mail(
                'BPM critique !!',
                'Attention, votre fréquence cardiaque est anormalement basse. Nous vous recommandons de consulter votre médecin dès que possible BPM critique = ' + str(self.bpm),
                'amine.berrfai@ump.ac.ma',
                ['amineberrfai62@gmail.com'],
                fail_silently=False,
            )
        return super().save(*args, **kwargs)


class PRESSION(models.Model):
    systolique = models.FloatField(null=True)
    diastolique = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)


    def get_dt_display(self):
        return self.dt.strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return str(self.systolique)

    def __str__(self):
        return str(self.diastolique)

    def save(self, *args, **kwargs):
        if self.systolique > 120:
            token = '5877186104:AAESpMPMIk6dvUILilf3aJ68Winv-79W36Q'
            rece_id = 1913801730
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id,'Attention, votre pression systolique est anormalement elevée. Nous vous recommandons de consulter votre médecin dès que possible. Presion systolique = ' + str(self.systolique))
            send_mail(
                'PRESSION critique !!',
                'Attention, votre pression systolique est anormalement elevée. Nous vous recommandons de consulter votre médecin dès que possible. Presion systolique = ' + str(self.systolique),
                'amine.berrfai@ump.ac.ma',
                ['amineberrfai62@gmail.com'],
                fail_silently=False,
            )
        if self.diastolique < 80:
            token = '5877186104:AAESpMPMIk6dvUILilf3aJ68Winv-79W36Q'
            rece_id = 1913801730
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id,'Attention, votre pression systolique est anormalement elevée. Nous vous recommandons de consulter votre médecin dès que possible. Presion diastolique = ' + str(self.diastolique))
            send_mail(
                'BPM critique !!',
                'Attention, votre pression systolique est anormalement elevée. Nous vous recommandons de consulter votre médecin dès que possible. Presion diastolique = ' + str(self.diastolique),
                'amine.berrfai@ump.ac.ma',
                ['amineberrfai62@gmail.com'],
                fail_silently=False,
            )
        return super().save(*args, **kwargs)



class Temp(models.Model):
    temp = models.FloatField(null= True)
    dt = models.DateTimeField(auto_now_add=True, null=True)

    def get_dt_display(self):
        return self.dt.strftime('%Y-%m-%d %H:%M:%S')

    def save(self, *args, **kwargs):
        if self.temp > 40:
            token = '5877186104:AAESpMPMIk6dvUILilf3aJ68Winv-79W36Q'
            rece_id = 1913801730
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id,'Cher patient, nous avons détecté que votre rythme cardiaque est supérieur à 40°C. Nous vous recommandons de consulter votre médecin dès que possible pour évaluer votre état de santé. Si vous ressentez des symptômes tels que des vertiges ou des douleurs thoraciques, veuillez contacter immédiatement votre médecin ou les services d"urgence. Prenez soin de vous. Temperature = ' + str(self.temp))
            send_mail(
                'BPM critique !!',
                'Cher [nom du patient], nous avons détecté que votre rythme cardiaque est supérieur à 100 bpm. Nous vous recommandons de consulter votre médecin dès que possible pour évaluer votre état de santé. Si vous ressentez des symptômes tels que des vertiges ou des douleurs thoraciques, veuillez contacter immédiatement votre médecin ou les services d"urgence. Prenez soin de vous.. Temperature = ' + str(self.temp),
                'amine.berrfai@ump.ac.ma',
                ['amineberrfai62@gmail.com'],
                fail_silently=False,
            )
        elif self.temp < 36:
            token = '5877186104:AAESpMPMIk6dvUILilf3aJ68Winv-79W36Q'
            rece_id = 1913801730
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id,'Attention, votre fréquence cardiaque est anormalement basse. Nous vous recommandons de consulter votre médecin dès que possible. Temperature = ' + str(self.temp))
            send_mail(
                'BPM critique !!',
                'Attention, votre fréquence cardiaque est anormalement basse. Nous vous recommandons de consulter votre médecin dès que possible Temperature = ' + str(self.temp),
                'amine.berrfai@ump.ac.ma',
                ['amineberrfai62@gmail.com'],
                fail_silently=False,
            )
        return super().save(*args, **kwargs)