import { HttpErrorResponse, HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { MatDialog } from "@angular/material/dialog";
import { Observable, throwError } from "rxjs";
import { ErrorDialog } from "../components/error.dialog";
import { catchError, finalize } from "rxjs/operators";

@Injectable()
export class HttpErrorService implements HttpInterceptor {
    constructor(private dialog: MatDialog) {}

    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        return next.handle(req).pipe(
            catchError(error => {
                this.dialog.open(ErrorDialog, { data: error });
                return throwError(error);
            }),
        );
    }
}