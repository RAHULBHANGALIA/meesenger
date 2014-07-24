from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as_
from django.template.defaultfilters import filesizeformat

class UploadForm(forms.Form):
    upload = form.FileField()

    def clean_upload(self):
        upload = self.cleaned_data['upload']
        content_type = upload.cotent_type
        if cotent_type in settings.CONTENT_TYPES:
            if upload_size > settgs.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(_('Please keep filesize under %s.Current filesize %s')%(filesizeformat(settings.MAX_UPLOAD_SIZE),filesizeformat(upload._size)))                        
        else:
            raise forms.ValidationError(_('File type is not supported'))

        return upload
class FileUploadForm(forms.Form):
    audio_file = forms.FileField(label = _(u"Audio File"))

    def clean(self):
        cleaned_data = self.cleaned_data
        file = cleaned_data.get("audio_file")
        file_exts = ('.mp3',)

        if file is None:
            raise forms.ValidationError('Please select file first')
        if not cotent_type in settings.CONTENT_TYPES:
            raise forms.ValidationError('Audio accepted  only in: %s' % ''.join( file_exts))

        return cleaned_data    
                                            
