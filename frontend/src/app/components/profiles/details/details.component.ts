import { Component, OnInit } from '@angular/core';
import { AngularFirestore } from '@angular/fire/compat/firestore';
import { ActivatedRoute } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { ProfileService } from 'src/app/services/profile.service';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.scss']
})
export class DetailsComponent implements OnInit {

  title = 'TEJO | IT Profiles';
  Employee: any;
  error: any;
  userEmail: string | undefined;
  paymentHandler: any;
  EmployeeName: string | undefined;
  ImageUrl: string | undefined;
  Working: any;
  user: any;
  Location: string | undefined;
  Expected_Sallary: string | undefined;
  Bio: string | undefined;
  mediaLocation = 'https://frontend.com/backend/';
  WorkExperience2_title: any;
  lista = ['Employed', 'Unemployed', 'Looking for new Opportunities'];
  // loggedIn: boolean;
  uEmail = localStorage.getItem('Uemail');
  uName = localStorage.getItem('Uname');
  message: any;
  github: any;
  youtube: any;
  linkedin: any;
  portfolio: any;
  // ModalTitle:string;
  ActivateAddEditDepComp:boolean=false;
  

  constructor(
    private route: ActivatedRoute, 
    private service: ProfileService,
    private db:AngularFirestore,
    private loginService: AuthService
  ) { }

  ngOnInit(): void {
    this.loadEmployee();
    this.getUser();
  }  


  loadEmployee(){
    const EmployeeId = this.route.snapshot.paramMap.get('id');
    this.service.getEmployee(EmployeeId).subscribe(
      (data) => {
        this.Employee = data[0];
        this.ImageUrl = this.mediaLocation + this.Employee.PhotoFileName;
      }, 
      error => {
        this.error = error;
      }
    );         
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

  updateLocation(){    
    let myId = this.route.snapshot.paramMap.get('id');
    var val = {
      EmployeeId: myId,
      EmployeeName: this.Employee.EmployeeName,
      Email: this.Employee.Email,
      Location:this.Location || this.Employee.Location,
      Expected_Sallary: this.Expected_Sallary || this.Employee.Expected_Sallary,
      Working: this.Working || this.Employee.Working,
      Bio: this.Bio || this.Employee.Bio,
      github: this.github || this.Employee.github || '',
      youtube: this.youtube || this.Employee.youtube || '',
      linkedin: this.linkedin || this.Employee.linkedin || '',
      portfolio: this.portfolio || this.Employee.portfolio || ''      
    };
    this.service.updateEmployeeLocation(val).subscribe(res=>{
        alert(res.toString());
    this.Employee = res;
    this.loadEmployee();
    /*
    document.getElementById("updateBio").style.display = "None"; 
    document.getElementById("updateLocation").style.display = "None";
    document.getElementById("updateSallary").style.display = "None";
    document.getElementById("updateAvai").style.display = "None";
    document.getElementById("updateSocials").style.display = "None";
    */
    });
  }

  

  

}
