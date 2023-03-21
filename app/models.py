from django.db import models
from django.urls import reverse
 
class Event(models.Model): 
    CATEGORY_CHOICES = [ ('Birthday', 'Birthday'), ('Public Holiday', 'Public Holiday'), ('Event', 'Event'), ('Others', 'Others'),]
    visibility = models.BooleanField(default=False ) 
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()
    @property
    def get_event_description(self):
          
        des =Event.objects.get(id = self.id,description = self.description) 
        try:
            des =Event.objects.get(id = self.id,description = self.description)
            return des.description
        except:
            return False
     
    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> <span class ="options" style="  margin-top:1px;color:#707070;  " > <img class="img1"style="width:20px; height:20px;" src="../static/assets/img/edit.png" alt="edit"/> </span></a><br> '
    @property
    def deleteEvent(self):  
        urls = reverse('event_delete', args=(self.id,))
        return f'<br><a href="{urls}"> <span class ="options"id = "options"  > <img class="img2"style="width:20px; margin-top:10px;color:#707070;"src="../static/assets/img/delete.png" alt="delete"/> </span></a>'
        # return f'<br><button id="primaryButton{cot}" href="{urls}" ></button>' 
        # return f'<br> <a data-bs-toggle="modal" data-bs-target="#sureModal"> <span class ="options" style="  margin-top:20px;color:#707070;" > <img class="img2"style="width:20px; margin-top:10px;color:#707070;"src="../static/assets/img/delete.png" alt="delete"/> </span></a><div class="modal fade" id="sureModal" tabindex="-1" aria-labelledby="sureModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="modal-header"><h5 class="modal-title" id="sureModalLabel">Are you Sure?</h5></div> <div class="modal-footer"><button type="button" style="background-color:red;" class="btn btn-danger" data-bs-dismiss="modal">No</button><a href="{urls}" class="btn btn-primary">Yes</a></div></div></div></div>'
        # return f'<br><button hidden id="primaryButton" href="{urls}"></button><a data-bs-toggle="modal" data-bs-target="#sureModal"> <span class ="options" style="  margin-top:20px;color:#707070;" > <img class="img2"style="width:20px; margin-top:10px;color:#707070;"src="../static/assets/img/delete.png" alt="delete"/> </span></a><div class="modal fade" id="sureModal" tabindex="-1" aria-labelledby="sureModalLabel" aria-hidden="true"> <div class="modal-dialog"> <div class="modal-content"> <div class="modal-header"><h5 class="modal-title" id="sureModalLabel">Are you Sure?</h5></div> <div class="modal-footer"><button type="button" style="background-color:red;" class="btn btn-danger" data-bs-dismiss="modal">No</button><button type="button" id='"secondaryButton"' class="btn btn-primary" onclick="document.getElementById("primaryButton").click()">Yes</button></div></div></div></div>'
    


        