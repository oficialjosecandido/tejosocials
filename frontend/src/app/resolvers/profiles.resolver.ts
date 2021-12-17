import { Injectable } from '@angular/core';
import {
  Router, Resolve,
  ActivatedRouteSnapshot
} from '@angular/router';
import { EMPTY, Observable } from 'rxjs';
import { ProfileService } from '../services/profile.service';
import { Profiles } from './profiles';
import { catchError, delay } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ProfilesResolver implements Resolve<Profiles> {
  constructor(
    private profiles: ProfileService, private router: Router
  ) {}
  resolve(_route: ActivatedRouteSnapshot): Observable<any> {
    return this.profiles.getEmpList().pipe(
      delay(3000),
      catchError(() =>{
        this.router.navigate([""]);
        return EMPTY;
      })
    )
  }
}
