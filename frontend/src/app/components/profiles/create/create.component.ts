import { Component, Input, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { ProfileService } from 'src/app/services/profile.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateComponent implements OnInit {
  profileForm: FormGroup;

  @Input() emp:any;
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
  Primary_Tech: any;
  Bio: string | undefined;
  WorkExperience1_title: any;
  WorkExperience1_startYear: any;
  WorkExperience1_startMonth: any;
  WorkExperience1_endYear: any;
  WorkExperience1_endMonth: any;
  WorkExperience1_techs: any;
  WorkExperience1_company: any;
  WorkExperience1_companyLink: any;
  WorkExperience1_description: any;
  PhotoFileName:string | undefined;
  PhotoFilePath:string | undefined;
  Email: string | undefined;  

  EmployeeId: any;
  Department: any;
  uEmail: any;
  DepartmentsList:any=[];
  lista = ['Full-Stack Developer', 'Front-End Developer', 'Back-End Developer', 'Mobile Developer', 'Data Analyst', 'Data Engineer', 'DevOps', 'Product/Project Manager', 'UI/UX Designer', 'Web Developer'
          , 'Tester/Quality', 'Cloud Engineer', 'Network Engineer', 'AI Engineer', 'Machine Learning Engineer'];
  avais = ['Employed', 'Unemployed', 'Looking for Opportunities']
  WorkExperience2_title: any;
  loggedIn: boolean | undefined;


  constructor(
    public profileService: ProfileService,
    public formBuilder: FormBuilder,
    public router: Router,
  ) { 
    this.profileForm = formBuilder.group({
      name: [''],
      primaryTech: ['']
    })
   }

  ngOnInit(): void {
  }


  addEmployee(){
    // let email = localStorage.getItem('user email');
    var val = {
      EmployeeId:this.EmployeeId,
      EmployeeName:this.EmployeeName,
      Department:this.Department,
      PhotoFileName:this.PhotoFileName,
      Primary_Tech: this.Primary_Tech,
      Location: this.Location,
      Bio: this.Bio,
      Working: this.Working,
      Email: 'tste@teste.com',
      github: '',
      linkedin: '', 
      youtube: '',
      portfolio: ''    
    };
    this.profileService.createProfile(val).subscribe(res=>{
      alert(res.toString());
    });
    this.router.navigate(['/']);
  }

  uploadPhoto(event: any){
    var file=event.target.files[0];
    const formData:FormData=new FormData();
    formData.append('uploadedFile',file,file.name);

    this.profileService.UploadPhoto(formData).subscribe((data:any)=>{
      this.PhotoFileName=data.toString();
      this.PhotoFilePath=this.profileService.PhotoUrl+this.PhotoFileName;
    })
  }
  

}
