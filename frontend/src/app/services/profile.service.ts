import { Injectable } from '@angular/core';
import { AngularFirestore } from '@angular/fire/compat/firestore';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import { environment } from 'src/environments/environment';


@Injectable({
  providedIn: 'root'
})
export class ProfileService {
  readonly APIUrl =  environment.apiKey;
  readonly PhotoUrl = environment.apiKey;
  
  constructor(private http:HttpClient) { }

  getEmpList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/employee/');
  }

  createProfile(val:any){
    return this.http.post(this.APIUrl + '/employee/',val);
  }

  UploadPhoto(val:any){
    return this.http.post(this.APIUrl+'/SaveFile',val);
  }

  getEmployee(value: any):Observable<any> {
    return this.http.get(this.APIUrl+`/profile/${value}`);
  }

  updateEmployeeLocation(val:any){
    console.log('o que enviei', val);
    return this.http.put(this.APIUrl + '/employee/',val);
  } 
}
