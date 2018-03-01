import React from "react"

export default class GithubRepos extends React.Component {
  render() {
    let {repos} = this.props
    let repoNodes = []
    let lol = 1
    repos.forEach((item, index) => {
      let node = (
        <div key={lol}>{item.fo}</div>
      )
      lol = lol + 1
      repoNodes.push(node)
    })

    return (
      <div>{repoNodes}</div>
    )
  }
}
