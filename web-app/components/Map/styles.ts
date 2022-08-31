import styled from 'styled-components'

export const Wrapper = styled.div`
  width: 100%;
  height: 100%;

  .leaflet-container {
    background-color: var(--background);
  }
`
export const Container = styled.div`
  width: 100%;
  height: 100%;
`

export const Title = styled.h1`
  font-size: 2.5rem;
  position: fixed;
  z-index: 1100;
  top: var(--medium);
  right: var(--medium);
  color: var(--highlight);
`
