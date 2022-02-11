import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from "@angular/router";
import { Router } from '@angular/router';

@Component({
  selector: 'app-course',
  templateUrl: './course.component.html',
  styleUrls: ['./course.component.scss']
})
export class CourseComponent implements OnInit {

  course:any;

  constructor(private http: HttpClient, private route: ActivatedRoute, private router: Router) { }

  courses_endpoint() {
    return this.http.get('http://localhost:3000/courses');
  }

  ngOnInit(): void {
    this.router.routeReuseStrategy.shouldReuseRoute = () => {
      // do your task for before route

      return false;
    }

    this.courses_endpoint().subscribe((res) => {
      let courses:any = res;
      this.course = courses.filter((c: any) => c.id == this.route.snapshot.paramMap.get("id"))[0]
      console.log(this.course)
    })
  }

}
