import { Component, OnInit } from '@angular/core';
import { PostsService } from 'src/app/services/posts.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  title: any;
  postsList: any=[];
  sanitizer: any;
  j: any;

  

  constructor(private posts:PostsService) { }

  ngOnInit(): void {
    this.getPosts();
  }

  getPosts() {
    this.posts.getHomePosts().subscribe(data=>{
      this.postsList=data;
      console.log(data);
    });
  }

  

}
