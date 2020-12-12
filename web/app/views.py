from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
import requests




class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserSendTokensView(UpdateView):
    model = User
    fields = '__all__'
    template_name = 'send_tokens.html'


    def get_context_data(self, **kwargs):
        context = super(UserSendTokensView, self).get_context_data(**kwargs)
        current_user = User.objects.get(pk=self.kwargs['pk'])

        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        # print("The user email is : {} ".format(current_user.email))

        url = "https://sup.evloader.com/api/wallet/sup-points"
        payload = {
            "user_email": current_user.email,
            "token_amount": current_user.profile.tokens_amount
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        # print(response)

        # update the token_amount field
        # current_user.token_amount -= current_user.token_amount
        # current_user.save()


        context['user'] = user

        return render(request, template_name, context)
        #return context




        

        