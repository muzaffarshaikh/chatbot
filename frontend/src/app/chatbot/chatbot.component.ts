import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormGroup, FormControl} from '@angular/forms';
import { formatDate } from '@angular/common';
import { Router } from '@angular/router';
import { LoginComponent } from '../account/login.component';


declare const chat: any;
declare const modal_close: any;
declare const diable_back_button:any;

@Component({
  // selector: 'app-chat1',
  providers:[LoginComponent ],
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})


export class ChatbotComponent  {
  submitted = false;
  user_fname: string;
  user_lname : string;
  bot_response : string;
  textbox;
  logdet
  reply: string;

  public message: FormGroup; 
  public edit_profile_form: FormGroup;
  loading = true
  
  today_frontend = Date.now();
  fixedTimezone = this.today_frontend;
    
  time_stamp(){
    const today1= new Date();
    const time1 = formatDate(today1, 'hh:mm a', 'en-US', '+0530');
    return time1
  }
 
  my_leaves(){
        var time = this.time_stamp()
        console.log(time)
        var val=({"userinput" : "My leaves"})
        console.log(val);
        this.http.post('http://localhost:5000/input_buttons/ ', val).subscribe((response)=>{
          let bot_response=response["response"]; 
          let user_input=response["userinput"];
          console.log(bot_response);

          chat(bot_response, user_input, time) 
        });
  }

  Off_days(){
        var time = this.time_stamp()
        console.log(time)
        var val=({"userinput" : "Off days"})
        console.log(val);
        this.http.post('http://localhost:5000/input_buttons/ ', val).subscribe((response)=>{
          let bot_response=response["response"]; 
          let user_input=response["userinput"];
          console.log(bot_response);

          chat(bot_response, user_input, time) 
        });
  }

  my_profile(){
        var time = this.time_stamp()
        console.log(time)
        var val=({"userinput" : "my profile"})
        console.log(val);
        this.http.post('http://localhost:5000/input_buttons/ ', val).subscribe((response)=>{
          let bot_response=response["response"]; 
          let user_input=response["userinput"];
          console.log(bot_response);

          chat(bot_response, user_input, time) 
        });
  }

  send(){//messages
    
    var time = this.time_stamp()
    console.log(time)
    console.log(this.message.value); 
    var val=this.message.value;
    this.http.post('http://localhost:5000/input_data/ ', val).subscribe((response)=>{
        let bot_response=response["response"]; 
        let user_input=response["userinput"];
        let user_email=response["email"]
        console.log(bot_response);
        console.log(user_email);
    
        // setTimeout(chat(bot_response,user_input,time),90000000 )
        chat(bot_response,user_input,time) 
        this.message.reset();
        
      });
  }
  
  onSave(){
    console.log(this.edit_profile_form.value);//printing the user profile details
    var new_info = this.edit_profile_form.value;
    this.http.post('http://localhost:5000/edit_user_info/ ', new_info).subscribe((response)=>{
    let new_user_fname=response["new_user_fname"]; 
    let new_user_lname=response["new_user_lname"];
    this.reply=response["msg"];
    console.log(new_user_fname,new_user_lname);
  });
  }

  closemodal(){
    modal_close()
  }

  onLogout(){
    let out=false
    this.router.navigate(['/account/login']);
    this.http.post('http://localhost:5000/logged_out_user/ ', out).subscribe((response)=>{
    let res=response["response"]; 
    console.log(res);
  });
  }

  constructor(private readonly http: HttpClient , private router: Router, private logcomp:LoginComponent ) {
     
    diable_back_button()

     this.message = new FormGroup({
      'userinput': new FormControl('')
    });
    
    this.edit_profile_form = new FormGroup({
      'user_image': new FormControl(''),
      'user_fname': new FormControl(''),
      'user_lname': new FormControl('')
    });


    //getting user details from backend
    this.http.get('http://localhost:5000/user_info/ ').subscribe((response)=>{
    let user_fname=response["user_fname"]; 
    let user_lname=response["user_lname"];
    this.user_fname=user_fname
    this.user_lname=user_lname
    console.log(this.user_fname,this.user_lname);
  }); 
 }
    
}


  


