import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Col, Container, Form } from 'react-bootstrap';
import { AiFillPicture } from "react-icons/ai";
import WriteTweet from './Components/WriteTweet';
import Tweet from './Components/Tweet';
import Pallete from './Components/Pallete';
import useApiCallback from './customHooks/useApiCallback'
import axios from 'axios';
import { useEffect } from 'react';
function App() {


  const request = useApiCallback(() => axios.get('http://127.0.0.1:8000/tweets/'), (data) => console.log(data))

  useEffect(() => {
    request.request()
  }, [])


  return (
    <div className="App" style={{backgroundColor : Pallete.primary}}>
      <div className="container p-4">
        <WriteTweet></WriteTweet>

        <Tweet>
        </Tweet>
        <Tweet>
        </Tweet>
        <Tweet>
        </Tweet>
        <Tweet>
        </Tweet>



      </div>
    </div>
  );
}

export default App;
