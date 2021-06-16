import { ModelInterface } from "./model.interface";

export class UserModel implements ModelInterface {
    constructor(
        public id: number,
        public email: string,
        public username: string,
        public password: string,
    ) {}
}