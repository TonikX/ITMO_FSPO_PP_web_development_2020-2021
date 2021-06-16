import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from "./components/app.component";
import { LoginComponent } from "./components/login.component";
import { MainComponent } from "./components/main.component";
import { AppRoutingModule } from "./app-routing.module";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { ReactiveFormsModule } from "@angular/forms";
import { MatInputModule } from "@angular/material/input";
import { MatCardModule } from "@angular/material/card";
import { MatButtonModule } from "@angular/material/button";
import { MatToolbarModule } from "@angular/material/toolbar";
import { MatSidenavModule } from "@angular/material/sidenav";
import { MatIconModule } from "@angular/material/icon";
import { MatListModule } from "@angular/material/list";
import { MatTableModule } from "@angular/material/table";
import { MatPaginatorModule } from "@angular/material/paginator";
import { MatSortModule } from "@angular/material/sort";
import { MatProgressSpinnerModule } from "@angular/material/progress-spinner";
import { HTTP_INTERCEPTORS, HttpClientModule } from "@angular/common/http";
import { MatDialogModule } from "@angular/material/dialog";
import { AuthorsComponent } from "./components/crud/authors/authors.component";
import { CrudService } from "./services/crud.service";
import { AuthorDialog } from "./components/crud/authors/author.dialog";
import { DeleteDialog } from "./components/crud/delete.dialog";
import { BooksComponent } from "./components/crud/books/books.component";
import { BookDialog } from "./components/crud/books/book.dialog";
import { ErrorDialog } from "./components/error.dialog";
import { HttpErrorService } from "./services/http.error.service";
import { BorrowersComponent } from "./components/crud/borrowers/borrowers.component";
import { BorrowerDialog } from "./components/crud/borrowers/borrower.dialog";

@NgModule({
    declarations: [
        AppComponent,
        LoginComponent,
        MainComponent,
        AuthorsComponent,
        AuthorDialog,
        BooksComponent,
        BookDialog,
        BorrowersComponent,
        BorrowerDialog,
        DeleteDialog,
        ErrorDialog,
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        BrowserAnimationsModule,
        ReactiveFormsModule,
        MatInputModule,
        MatCardModule,
        MatButtonModule,
        MatToolbarModule,
        MatIconModule,
        MatSidenavModule,
        MatListModule,
        MatTableModule,
        MatPaginatorModule,
        MatSortModule,
        MatProgressSpinnerModule,
        HttpClientModule,
        MatDialogModule,
    ],
    providers: [
        { provide: HTTP_INTERCEPTORS, useClass: HttpErrorService, multi: true },
        { provide: 'AuthorService', useClass: CrudService },
        { provide: 'BookService', useClass: CrudService },
        { provide: 'BorrowerService', useClass: CrudService },
    ],
    bootstrap: [AppComponent],
})
export class AppModule { }
