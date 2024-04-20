# profiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa  # type: ignore

from .models import Profile
from django.contrib.auth import logout


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# views.py
from django.contrib.auth.forms import UserCreationForm

# views.py
from django.http import HttpResponse
from django.template.loader import get_template


# views.py

from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from .models import Profile


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template("resume_template.html")
        profile = Profile.objects.get(
            user=request.user
        )  # Assuming user is linked to Profile
        context = {"profile": profile}
        html = template.render(context)
        pdf = self.convert_html_to_pdf(html)
        response = HttpResponse(pdf, content_type="application/pdf")
        response["Content-Disposition"] = 'filename="resume.pdf"'
        return response

    @staticmethod
    def convert_html_to_pdf(html):
        result = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
        if not pdf.err:
            return result.getvalue()
        return None


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful profile creation
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})


def generate_pdf(request):
    # Implement logic to generate PDF from profile data
    template_path = "profile_template.html"
    context = {}  # Add context data for profile
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="resume.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response


# profiles/views.py

from django.shortcuts import render


def homepage(request):
    return render(request, "homepage.html")



def register(request):
    # Define the view logic for the registration form
    return render(request, "register.html")


def view_profile(request):
    # Define the view logic for viewing the profile
    return render(request, "view_profile.html")


def generate_pdf(request):
    # Define the view logic for generating the PDF
    return render(request, "generate_pdf.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "login"
            )  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


# profiles/views.py


def registration_success(request):
    return render(request, "registration_success.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the new homepage after successful login
            return redirect("new_homepage")
        else:
            # Return an invalid login error message
            return render(
                request,
                "login.html",
                {"error_message": "Invalid username or password."},
            )
    else:
        return render(request, "login.html")


# views.py


def new_homepage(request):
    # Add any context data you want to pass to the template
    context = {
        # Add any context data here
    }
    return render(request, "new_homepage.html", context)


def logout_view(request):
    logout(request)
    return redirect("homepage")
