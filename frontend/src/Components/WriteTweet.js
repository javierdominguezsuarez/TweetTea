import React from 'react'
import { Col, Container, Form } from 'react-bootstrap';
import { AiFillPicture } from "react-icons/ai";

export default function WriteTweet() {
    return (
        <Col sm = {100} className="shadow-sm p-3" style={{backgroundColor : "white", borderRadius: 10}}>
          <textarea style={{width: "100%", border: 0, height: 120, resize: "none", outline: "none"}} placeholder="Escribe tu primer tweet..."></textarea>
          <div className="d-flex justify-content-between align-items-center">
            <AiFillPicture size={30} color="#a5a5a5" class="mt-3">   </AiFillPicture>
            <div style={{padding: "7px 40px", backgroundColor: "#ED553B", color: "white", fontWeight: 600, fontFamily : "Poppins" , borderRadius: 100}}>
              POST
            </div>
          </div>
        </Col>
    )
}
