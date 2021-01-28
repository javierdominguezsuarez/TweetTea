import React from 'react'
import { Col, Container, Form } from 'react-bootstrap';
import { AiFillPicture } from "react-icons/ai";
import Pallete from './Pallete';

export default function WriteTweet() {
    return (
        <Col sm = {100} className="p-3" style={{backgroundColor : Pallete.secondary, borderRadius: 10}}>
          <textarea style={{width: "100%", border: 0, height: 100, resize: "none", outline: "none", backgroundColor : Pallete.secondary, color : Pallete.textPrimary, }} placeholder="Escribe tu primer tweet..."></textarea>
          <div className="d-flex justify-content-between align-items-center">
            <AiFillPicture size={30} color={Pallete.textSecondary} class="mt-3">   </AiFillPicture>
            <div style={{padding: "7px 40px", backgroundColor: Pallete.mainColor, color: "white", fontWeight: 600, fontFamily : "Poppins" , borderRadius: 100}}>
              POST
            </div>
          </div>
        </Col>
    )
}
