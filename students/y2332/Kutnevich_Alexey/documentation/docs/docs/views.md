# Views

Представления реализованы через классы, за исключением выхода из аккаунта.


## Menu

    class Menu(ListView):
        model = Inspector
        template_name = 'home.html'

Данное представление выводит главную страницу - меню


## RentersList

    class RentersList(ListView):
        paginate_by = 3
        model = Renter
        template_name = 'renter_list.html'

Данное представление выводит лист плательщиков, ограничивая количество записей на странице до 3-ёх


## RentersRetrieveView

    class RentersRetrieveView(DetailView):
        model = Renter
        template_name = 'renter_detail.html'

Данное представление выводит подробную информацию о плательщике


## RenterCreate

    class RenterCreate(CreateView):
        model = Renter
        fields = '__all__'
        template_name = 'renter_create.html'
        success_url = '/renters/'

Данное представление выводит форму создания плательщика, а затем перенапраляет пользователя на лис плательщиков


## RenterUpdate

    class RenterUpdate(UpdateView):
        model = Renter
        form_class = RenterForm
        template_name = "renter_update.html"
        success_url = '/renters/'

Данное представление выводит форму обновления плательщика, а затем перенапраляет пользователя на лис плательщиков


## RenterDeleteView

    class RenterDeleteView(DeleteView):
        model = Renter
        template_name = "renter_delete.html"
        success_url = '/renters/'

Данное представление выводит подтверждение удаления плательщика, а затем перенапраляет пользователя на лис плательщиков

Для остальных моделей представления аналогичны


## RegisterUser

    class RegisterUser(CreateView):
        form_class = RegisterInspectorForm
        template_name = 'register.html'
        success_url = 'http://127.0.0.1:8000/menu/'

        def form_valid(self, form):
            user = form.save()
            login(self.request, user)
            return redirect('http://127.0.0.1:8000/menu/')

Данное представление, наследуясь от класса `CreateView`, выводит форму регистрации `RegisterInspectorForm` и после создания пользователя, сразу авторизирует его


## LoginUser

    class LoginUser(LoginView):
        form_class = LoginInspectorForm
        template_name = "login.html"

        def get_success_url(self):
            return reverse_lazy('home')

Данное представление, наследуясь от класса `LoginView`, выводит форму авторизации `LoginInspectorForm` и после входа, перенаправляет пользователя на главную страницу


## logout_user

    def logout_user(request):
        logout(request)
        return redirect('http://127.0.0.1:8000/menu/')

Данное представление служит для выхода из аккаунта