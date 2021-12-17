import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PostsService {
  readonly APIUrl =  environment.apiKey;

  constructor(private http:HttpClient) { }

  getHomePosts():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + 'getPosts/');
  }
  
}
