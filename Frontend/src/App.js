import './App.scss';
import { Container, Stack} from "@mui/material"
import React, { useState, useRef,useEffect} from "react";
import ImageFrame  from './components/ImageFrame';
import Button from 'react-bootstrap/Button';
import axios from 'axios';


export default function App() {

  const [page, setPage] = useState([
    {
      orderno: 1,
      "type": "",
      "source": ""
    }
  ])
  const [pages, setPages] = useState([]);
  const [currentPage, setCurrentpage] = useState(1);
  const [maxPageLength, setMaxLength] = useState(1);
  const ref = useRef(null);
  const url = 'http://10.30.0.21:8000/';
  
  // const [Image,setImage] = useState([]);
  // const {getRootProps, getInputProps, isDragActive} = useDropzone({
  //   accept :"image/*",
  //   onDrop: (acceptedFile) =>{
  //     setImage(
  //       acceptedFile.map((upFile)=> Object.assign(upFile,{
  //         preview: URL.createObjectURL(upFile)
  //       }))
  //     )
  //   }
  // })
 

  // adds new input
  const handleAdd = (index) => {
    setPage([
      ...page,
      {
        orderno: page.length + 1, 
      }
    ])
    
  
    // setMaxLength(maxPageLength + 1);
    // setMaxLength(page.length + 1);
    setCurrentpage(index);
    console.log(page);
    
  }
  // removes input
  const handleRemove = (index) => {
    if (page.length > 1) {
      setPage(page => page.filter((p, i) => i !== index));
      //  setPage(page.splice(index,1));
      console.log(page);
      
    }
    
  }
  
  const setPageContent = (source,type,index) => {
    page[index].source = source.name;
    page[index].type = type;
    setPage(page)
    const newPages = pages.slice();
    newPages.push(source);
    setPages(newPages);
    console.log("New Pages", newPages);
    console.log('Page Index',page[index]);
  }

  const saveChanges = () =>{
    
    const current = new Date();
  const date = `${current.getFullYear()}-${current.getMonth()+1}-${current.getDate()}`;
    //validation

    // const payloadTest = {"co_id": 1, "order_number": "Ic-4567", "page_details": {"order_id": "IC-56766"}, "version": "v2", "created_at": "2022-10-10", "updated_at": "2022-10-10"}

    const payload = {
      "co_id": 1,
      "order_number": "IC-12345",
      "page_details": {
          pages: page,
          "order_id": "IC-12345",
          "page_count": page.length
      },
      "version": "v1",
      "created_at": date ,
      "updated_at": date 
  }
  console.log('Page',page);
  fetch(url + 'Photobook', { 
      method: 'POST', 
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(payload) 

    }).then(res=> console.log(res))
    .catch((error) => {
      console.error(error);
    });


   
    let body = new FormData();
 
    body.append("file_name", "IC-1234");
    body.append("images", pages);
  
  fetch(url + 'upload',{ 
    method: 'POST',
    body :body
  }).then(res=> console.log(res))
  .catch((error) => {
    console.error(error);
  });
  console.log('File Content',pages);
  console.log(payload);
  console.log ('Date',date);
  }
  const handleSubmit = async(event) => {
    event.preventDefault()
    const formData = new FormData();
    formData.append("file_name", "IC-1234");
    formData.append("images", pages);
    try {
      const response = await axios({
        method: "post",
        url: url + 'upload',
        data: formData,
        headers: { "Content-Type": "multipart/form-data" },
      });
    } catch(error) {
      console.log(error)
    }
  }

  return (
      <Container className="App">
        <Stack spacing={2}>
          {page.map((item, index) => (
            <ImageFrame
              handleAdd={handleAdd}
              handleRemove={handleRemove}
              page={item}
              index={index}
              setPageContent = {setPageContent}
            />
          ))}
        </Stack>
        <Button variant="primary" className='save-btn' onClick={handleSubmit}>Save Album</Button>

      </Container>
    
  )
}
