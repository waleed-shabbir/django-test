from django.db import models


# Create your models here.
class BoardingPass(models.Model):
    source = models.CharField(max_length=100)
    journey_details = models.CharField(max_length=100,null=True, blank=True) # gate45B Seat 3A, etc
    destination = models.CharField(max_length=100)
    mode = models.CharField(max_length=100) # train, plane, bus, etc
    mode_details = models.CharField(max_length=100,null=True, blank=True) # # Sk22, 78A, etc

    def __str__(self):
        return str(self.source) + " " + str(self.destination)

    def __eq__(self, other):
        if not isinstance(other, BoardingPass):
            return NotImplemented
        if self._meta.concrete_model != other._meta.concrete_model:
            return False
        my_pk = self.pk
        if my_pk is None:
            return self is other
        return my_pk == other.pk

    def as_json(self):
        return {
            "source": self.source,
            "destination": self.destination,
            "mode": self.mode,
            "journey_details": self.journey_details,
            "mode_details": self.mode_details
        }
