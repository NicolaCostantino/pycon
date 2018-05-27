import * as React from 'react';
import { Button } from 'components/button';
import { Hero } from 'components/hero';
import { Title, Subtitle } from 'components/typography';

export const HomePage = () => (
  <>
    <Hero
      renderFooter={() => (
        <React.Fragment>
          <Button variant="secondary">Coming soon</Button>
        </React.Fragment>
      )}
    >
      <Title>PyCon 10</Title>
      <Subtitle>Florence, Italy</Subtitle>
      <Subtitle level={2}>May 2019</Subtitle>
    </Hero>
  </>
);
