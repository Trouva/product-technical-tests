import styled from "styled-components";

export const Icon = styled.div`
  text-align: center;
  height: 32px;
  width: 32px;
  min-width: 32px;
  max-width: 32px;
  position: relative;
`;

export const Content = styled.div`
  flex: 1;
`;

export const Wrapper = styled.div`
  align-items: center;
  color: var(--text-color);
  text-decoration: none;
  border-bottom: 1px solid var(--divider);
  cursor: pointer;
  display: flex;
  padding: var(--padding) var(--margin);
  gap: var(--padding);

  &:hover {
    background: rgba(0, 0, 0, 0.025);
  }
`;