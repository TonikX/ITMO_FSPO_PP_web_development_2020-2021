import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from "./components/login.component";
import { MainComponent } from "./components/main.component";
import { AuthorsComponent } from "./components/crud/authors/authors.component";
import { BooksComponent } from "./components/crud/books/books.component";
import { BorrowersComponent } from "./components/crud/borrowers/borrowers.component";

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  {
    path: 'main',
    component: MainComponent,
    children: [
      { path: 'authors', component: AuthorsComponent },
      { path: 'books', component: BooksComponent },
      { path: 'borrowers', component: BorrowersComponent },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
