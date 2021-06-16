import { ModelInterface } from "./model.interface";

export class AuthorModel implements ModelInterface {
    id: number;

    constructor(
        public name: string,
    ) {
        this.id = -1;
    }
}