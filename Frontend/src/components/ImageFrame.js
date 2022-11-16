import React, { createRef} from "react";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import AddPhotoAlternateOutlinedIcon from '@mui/icons-material/AddPhotoAlternateOutlined';
import DeleteOutlineOutlinedIcon from '@mui/icons-material/DeleteOutlineOutlined';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import FlipToFrontIcon from '@mui/icons-material/FlipToFront';
import FlipToBackIcon from '@mui/icons-material/FlipToBack';
import Dropzone from 'react-dropzone';
import IconButton from "@mui/material/IconButton";
import DeleteIcon from '@mui/icons-material/Delete';
import axios from 'axios';



class ImageFrame extends React.Component {

    constructor() {
      super();
      this.scollToRef = createRef();
      this.onDrop = (files) => {
        this.setState({files});
        console.log('File',files);
        this.props.setPageContent(files[0].name,"",this.props.index);
        this.setState(
            { file: URL.createObjectURL(files[0])});
      };
      this.state = {
        files: [],
        type:"",
        button: true
      };
      this.handleClick = this.handleClick.bind(this);
    
    }

    handleClick(){
        this.state.type="front-cover";
      }
    
   
    state = { file: ""};
    handleChange = (e) => {
      const url = 'http://10.30.0.21:8000/';

      // const formData = new FormData();
      // // formData.append("file_name", "IC-1234");
      // formData.append("images", e.target.files[0]);

      // axios.post(url + 'upload', formData, {
      //   headers: {
      //     "Content-Type": "multipart/form-data",
      //   } ,
      // })
      // .then((res) => {
      //   console.log(res.data);
      // })
      // .catch((err) => console.log(err));

      this.setState({ file: URL.createObjectURL(e.target.files[0])});
      console.log("File data",e.target.files[0]);
      this.props.setPageContent(e.target.files[0],this.state.type,this.props.index);
    }

    // onDrop = (acceptedFiles) => {
    //   // console.log(acceptedFiles);   
    //   this.file = acceptedFiles;
    //   this.setState({file:this.file[0].path});
    //   console.log(this.file[0].path); 
    // }
   
    
    render() {
      const files = this.state.files.map(file => (
        // <li key={file.name}>
        //   {file.name} - {file.path} bytes
        // </li>
        <img key={file.name} src={file.name}></img>
      ));
      
      return (
        <Row className="justify-content-md-center">
          <Col md={12} sm={12} className="image-frame">
            <div className='image-tools'>
              <p className="page-number">Page - {this.props.index +1}</p>
              <AddPhotoAlternateOutlinedIcon className='icon' onClick={this.props.handleAdd} > </AddPhotoAlternateOutlinedIcon>
              <DeleteOutlineOutlinedIcon className='icon' onClick={() => this.props.handleRemove(this.props.index)}></DeleteOutlineOutlinedIcon>
              <KeyboardArrowUpIcon className='icon'></KeyboardArrowUpIcon>
              <KeyboardArrowDownIcon className='icon' onClick={() => this.scollToRef.current.scrollIntoView()}></KeyboardArrowDownIcon>
              {/* <FlipToBackIcon className='icon'></FlipToBackIcon> */}
              
              {/* <FlipToFrontIcon className={this.state.button ? "buttonTrue": "icon"} onClick={this.handleClick}></FlipToFrontIcon> */}
              {/* <IconButton className= "icon">
        <FlipToFrontIcon   onClick={this.handleClick} />
      </IconButton> */}
              
            </div>
            <div className="image-container"  ref={this.scollToRef}>
            
              {/* <ul>{files}</ul> */}
            <Dropzone onDrop={this.onDrop} multiple>
            {({getRootProps, getInputProps,isDragActive}) => (
              
              <div {...getRootProps()} className="">
                <input {...getInputProps()} />
                <p>{isDragActive ? <p>Drop the image here..</p> : <p> Drag and Drop image here / click to select image</p>}</p>
                
              </div>
              
            )}
          </Dropzone>
          
              <div className='image-preview' style={{ backgroundImage: "url(" + this.state.file  + ")" }}></div>
            </div>
            <div>
              <label className='btn-grey' onChange={this.handleChange} htmlFor={"formId-" + this.props.index}>
                <input name="" type="file" id={"formId-" + this.props.index} hidden />
                Add Image
              </label>
            </div>
          </Col>
        </Row>
      )
    }
  }

  export default ImageFrame;