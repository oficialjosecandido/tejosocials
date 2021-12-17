import { Component } from '@angular/core';
import { AuthService } from './services/auth.service';
import {ModalDismissReasons, NgbModal} from '@ng-bootstrap/ng-bootstrap'; 


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Social Media';

  user:any;
  closeModal: string | undefined;

 
  

  constructor(
    private loginService: AuthService,
    private modalService: NgbModal,
  ) { }

  ngOnInit() { 

    this.loginService.getLoggedInUser()
      .subscribe( user => {
        console.log( user);
        this.user = user;
    }); 
  }

  loginGoogle(){
    console.log('Login...');
    this.loginService.login();
  }

  getMyData() {
    console.log('estás aqui', this.user.displayName);
  }

  logout(){
    this.loginService.logout();
  }

  triggerModal(content: any) {
    this.modalService.open(content, {ariaLabelledBy: 'modal-basic-title'}).result.then((res) => {
      this.closeModal = `Closed with: ${res}`;
    }, (res) => {
      this.closeModal = `Dismissed ${this.getDismissReason(res)}`;
    });
  }
  
  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return  `with: ${reason}`;
    }
  }

}
