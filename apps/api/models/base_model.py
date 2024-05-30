from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True

    def fill(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def save_with_validation(self):
        try:
            self.save()
            return True, "ok"  # Return True if save was successful
        except Exception as e:
            # Handle the exception as needed, e.g., logging
            print(f"Error saving object: {e}")
            return False,  f"Error saving object: {e}"