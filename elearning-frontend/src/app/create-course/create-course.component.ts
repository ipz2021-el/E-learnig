import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-create-course',
  templateUrl: './create-course.component.html',
  styleUrls: ['./create-course.component.scss']
})
export class CreateCourseComponent implements OnInit {

  constructor(private http: HttpClient, private router: Router) { }

  image = 'curriculum';
  title = '';
  tutor = '';
  description = '';
  tags = '';

  courses:any;

  courses_endpoint(body:any) {
    return this.http.post('http://localhost:3000/courses', body);
  }

  icons = ['curriculum', 'alcohol-burner', 'biotech', 'brain', 'calculator', 'computer', 'jupiter-planet', 'mobile', 'planetarium', 'story-book', 'student']

  ngOnInit(): void {}

  send() {
    let body = 
    {
      id: Date.now(),
      image: this.image,
      title: this.title,
      tutor: this.tutor,
      description: this.description,
      tags: this.tags,
      joined: false
    }
    this.courses_endpoint(body).subscribe((res) => {
      console.log(res);
      this.router.navigate(['/courses']);
    })
  }

}
