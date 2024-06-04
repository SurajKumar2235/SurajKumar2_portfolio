from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table="Messages"



from datetime import datetime
import os
def project_image_path(instance, filename):
    # Get the current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")
    # Generate the filename using the project name and the current date
    filename = f"{instance.prj_name}_{current_date}.jpg"  # Assuming the image is in JPG format
    # Return the full file path
    return os.path.join('project_images', filename)

class Projects(models.Model):
    prj_name=models.CharField(max_length=150,blank=False,null=False)
    short_desc=models.CharField(max_length=300)
    is_deleted=models.BooleanField(default=False)
    current_date=models.DateField(auto_now=True)
    updated_date=models.DateField(auto_now_add=True)
    prj_image=models.ImageField(upload_to=project_image_path)
    project_hosted_link=models.CharField(blank=True,null=True, max_length=500)
    def __str__(self):
        return self.prj_name
    

    def save(self, *args, **kwargs):
        # Check if the instance is being updated (already exists in the database)
        if self.pk:
            # If the project name has changed, update the image filename
            old_instance = Projects.objects.get(pk=self.pk)
            if old_instance.prj_name != self.prj_name:
                # Get the path of the old image
                old_image_path = old_instance.prj_image.path
                # Generate a new filename based on the updated project name
                new_filename = project_image_path(self, self.prj_image.name)
                # Rename the image file
                os.rename(old_image_path, os.path.join('media', new_filename))
                # Update the prj_image field with the new filename
                self.prj_image.name = new_filename

        super().save(*args, **kwargs)



    def delete(self,*args,**kwargs):
        self.is_deleted=True
        super().save(*args,**kwargs)

        
    class Meta:
        db_table="Project_Details"
