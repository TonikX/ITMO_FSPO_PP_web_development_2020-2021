import { Component, OnInit, TemplateRef, ViewChild } from '@angular/core';
import { AuthService } from "../services/auth.service";
import { UserModel } from "../models/user.model";
import { MatDialog } from "@angular/material/dialog";
import { Router } from "@angular/router";

@Component({
  selector: 'app-main',
  templateUrl: 'main.component.html',
  styleUrls: ['main.component.css'],
})
export class MainComponent implements OnInit {
  user?: UserModel;

  constructor(private auth: AuthService, private router: Router) { }

  ngOnInit() {
      this.auth.getCurrentUser().subscribe(
          user => this.user = user,
      );
  }

  logout() {
      this.auth.logout().subscribe(_ => {
          this.router.navigate(["/"]);
      });
  }
}
