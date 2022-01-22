import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit {

  constructor() { }

  mess = ''
  messages: string[] = [];

  send() {
    this.messages.push(this.mess);
    this.mess = '';
  }

  ngOnInit(): void {
  }

}
