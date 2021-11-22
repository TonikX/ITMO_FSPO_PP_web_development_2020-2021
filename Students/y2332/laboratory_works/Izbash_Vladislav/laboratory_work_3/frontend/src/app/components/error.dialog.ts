import { Component, Inject } from "@angular/core";
import { MAT_DIALOG_DATA } from "@angular/material/dialog";

@Component({
    selector: 'app-error-dialog',
    templateUrl: 'error.dialog.html',
})
export class ErrorDialog {
    message: string;

    constructor(@Inject(MAT_DIALOG_DATA) public error: any) {
        this.message = JSON.stringify(error.error);
    }
}