import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
// import { auth } from 'firebase/compat/app';
import { AngularFireAuth } from '@angular/fire/compat/auth';
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';



@Injectable({providedIn: 'root'})

export class AuthService {

  constructor(
    private afAuth: AngularFireAuth
  ) { }

  login() {
    console.log('Redirecting to Google login provider');
    this.afAuth.signInWithRedirect(new firebase.auth.GoogleAuthProvider());
  }

  getLoggedInUser() {
    return this.afAuth.authState;
  }

  logout() {
    this.afAuth.signOut();
  }

    
}
