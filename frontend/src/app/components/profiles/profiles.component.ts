import { ActivatedRoute } from '@angular/router';
import { Component, Input, OnInit } from '@angular/core';
import { AngularFirestore } from '@angular/fire/compat/firestore';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';
import { AuthService } from 'src/app/services/auth.service';

import { ProfileService } from 'src/app/services/profile.service';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-profiles',
  templateUrl: './profiles.component.html',
  styleUrls: ['./profiles.component.scss']
})
export class ProfilesComponent implements OnInit {

  data: any;
  profilesList:any=[];
  user: any;
  profiles: any;
  
  constructor(
    private profileService:ProfileService,
    private loginService:AuthService,
    private activatedRoute: ActivatedRoute
    ) { }

  ngOnInit(): void {
    this.profiles = this.activatedRoute.data.pipe(
      map(
        data => data?.profiles
      )
    )
    this.getProfiles();
    this.getUser();
    
    
  }

  getProfiles() {
    this.profileService.getEmpList().subscribe(data=>{
      this.profilesList=data;
      console.log(data);
    });
  }

  getUser() {
    this.loginService.getLoggedInUser().subscribe( 
      user => {
        this.user = user;
      }); 
  }

  tenhoUser() {
    // funciona!
    console.log('tenho user?', this.user?.displayName);
  }

}
  

