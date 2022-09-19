import './App.scss';
import { Button, Container, Divider, Stack, TextField } from "@mui/material"
import React, { useState } from "react";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import AddPhotoAlternateOutlinedIcon from '@mui/icons-material/AddPhotoAlternateOutlined';
import DeleteOutlineOutlinedIcon from '@mui/icons-material/DeleteOutlineOutlined';

class ImageFrame extends React.Component {

  state = { file: "" };
  handleChange = (e) => {
    this.setState({ file: URL.createObjectURL(e.target.files[0]) });
  }

  render() {
    return (
      <Row className="justify-content-md-center">
        <Col md={6} sm={12}>
          <div className='image-tools'>
            <p>{this.props.index + 1}</p>
            <AddPhotoAlternateOutlinedIcon className='icon' onClick={this.props.handleAdd} > </AddPhotoAlternateOutlinedIcon>
            <DeleteOutlineOutlinedIcon className='icon' onClick={() => this.props.handleRemove(this.props.index)}></DeleteOutlineOutlinedIcon>
          </div>
          <div className="image-container">
            <div className='image-preview' style={{ backgroundImage: "url(" + this.state.file + ")" }}></div>
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


export default function App() {

  const [page, setPage] = useState([
    {
      pageNumber: ""
    }
  ])

  // adds new input
  const handleAdd = () => {
    setPage([
      ...page,
      {
        pageNumber: ""
      }
    ])
  }
  // removes input
  const handleRemove = (index) => {
    if (page.length !== 1) {
      setPage(page.splice(index, 1));
    }
  }

  return (
    <>
      <Container className="App">
        <Stack spacing={2}>
          {page.map((item, index) => (
            <ImageFrame
              handleAdd={handleAdd}
              handleRemove={handleRemove}
              page={page}
              index={index}
            />
          ))}
        </Stack>

      </Container>
    </>
  )
}
