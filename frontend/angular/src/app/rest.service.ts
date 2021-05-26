import { Injectable } from '@angular/core';
import { Responses } from '../app/responses'
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http : HttpClient) { }

  user_responses: string = "http://127.0.0.1:5000/user_response/"
  // user_reponses : string = "http://127.0.0.1:5000/user_response"

  readuserresponses()
  {
    return this.http.get<Responses[]>(this.user_responses)
  }
}
