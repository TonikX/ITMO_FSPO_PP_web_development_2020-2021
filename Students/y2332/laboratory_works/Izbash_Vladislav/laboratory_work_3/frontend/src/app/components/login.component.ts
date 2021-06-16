import { Component, Inject, OnInit } from '@angular/core';
import { FormControl, FormGroup } from "@angular/forms";
import { Router } from "@angular/router";
import { AuthService } from "../services/auth.service";

@Component({
    selector: 'app-login',
    templateUrl: 'login.component.html',
    styleUrls: [ 'login.component.css' ],
})
export class LoginComponent implements OnInit {
    form = new FormGroup({
        username: new FormControl(''),
        password: new FormControl(''),
    });
    loginError?: any;

    constructor(private router: Router, private auth: AuthService) { }

    ngOnInit() { }

    login() {
        this.auth.login(this.form.value.username, this.form.value.password).subscribe(
            _ => this.router.navigate(['main/authors']),
            error => this.loginError = error.error,
        );
    }
}
